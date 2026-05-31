import streamlit as st
import pandas as pd

from database import (
    get_all_complaints
)

from utils.charts import (
    category_chart,
    priority_chart,
    status_chart
)

from utils.export import (
    dataframe_to_csv
)

# -------------------------
# LOGIN CHECK
# -------------------------


if (
    "user" not in st.session_state
    or st.session_state.user is None
):

    st.warning(
        "Please login first"
    )

    st.stop()

# -------------------------
# LOAD DATA
# -------------------------

rows = get_all_complaints()

columns = [
    "id",
    "name",
    "location",
    "issue",
    "category",
    "priority",
    "status",
    "image_path",
    "created_at"
]

df = pd.DataFrame(
    rows,
    columns=columns
)

# -------------------------
# PAGE
# -------------------------

st.title("📊 Dashboard")

# -------------------------
# METRICS
# -------------------------

col1, col2, col3 = st.columns(3)

total = len(df)

resolved = (
    len(
        df[
            df["status"] == "Resolved"
        ]
    )
    if len(df) > 0
    else 0
)

pending = (
    len(
        df[
            df["status"] != "Resolved"
        ]
    )
    if len(df) > 0
    else 0
)

col1.metric(
    "Total Complaints",
    total
)

col2.metric(
    "Resolved",
    resolved
)

col3.metric(
    "Pending",
    pending
)

# -------------------------
# FILTERS
# -------------------------

if len(df) > 0:

    search = st.text_input(
        "🔍 Search Complaint"
    )

    if search:

        df = df[
            df["issue"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

# -------------------------
# TABLE
# -------------------------

st.subheader(
    "All Complaints"
)

if len(df) == 0:

    st.info(
        "No complaints found"
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )

# -------------------------
# EXPORT
# -------------------------

if len(df) > 0:

    csv = dataframe_to_csv(df)

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="complaints.csv",
        mime="text/csv"
    )

# -------------------------
# CHARTS
# -------------------------

if len(df) > 0:

    st.subheader(
        "Category Distribution"
    )

    fig1 = category_chart(df)

    if fig1:
        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    st.subheader(
        "Priority Distribution"
    )

    fig2 = priority_chart(df)

    if fig2:
        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.subheader(
        "Status Distribution"
    )

    fig3 = status_chart(df)

    if fig3:
        st.plotly_chart(
            fig3,
            use_container_width=True
        )