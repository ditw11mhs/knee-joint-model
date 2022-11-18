import streamlit as st


def main():
    st.header("Knee Joint Model Parameter Identification")
    st.subheader("Biocybernetics")
    st.markdown("Aditya Wardianto 07311940000001")
    st.markdown(
        """
                Knee joint model parameter identification, program development:
                1.	Motion equation of knee joint (with passive joint parameters).
                2.	Expression of model parameter identification (objective functions, and gradients)
                3.	Skeleton program of model simulation of movement (RKIV integration method, visualization)
                4.	Optimization program to identify the parameters
                5.	Integration program
                """
    )
    st.markdown("Made with ❤️, 🦾,  and ☕")


if __name__ == "__main__":
    main()
