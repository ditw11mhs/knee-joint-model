import streamlit as st

from api import logic, utils


def main():
    st.header("App")
    file = st.file_uploader("Upload file here")
    if file is not None:
        df = utils.open_file(file)
        st.dataframe(df)
        st.line_chart(df, x="Time", y="Angle")


if __name__ == "__main__":
    main()
