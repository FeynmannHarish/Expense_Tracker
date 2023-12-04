import streamlit as st
import graphviz

tab1,tab2,tab3,tab4 = st.tabs(["About","Hobbies","Contact","How to use this app ?"])

with tab1:
    col1,col2 = st.columns([0.3,0.7])
    with col1:
        st.image("my_picture/harish.jpg",width=200)
    
    st.subheader("Harish Ravi :sunglasses:")
    
    with col2:
        st.write("Hello, I am Harish Ravi, a junior developer :computer: . My parents find it challenging to manage and track their expenses. So, I created a website  to help them in tracking and managing their expenses. You can use this website to manage and track your expenses as well. I hope you all like it.")

with tab2:
     st.write("I love solving math :triangular_ruler: problems and watching documentaries 	:performing_arts: to learn about different things. Also, I'm into MMA fights :boxing_glove: , enjoying the intensity and skills of the fighters.")

with tab3:
    st.write("Email : harishmaths.ai@gmail.com")
    st.write("Website : https://harishmaths.home.blog/")

with tab4:
    graph = graphviz.Digraph()

    graph.edge("Click Add Expense tab","Fill Date")
    graph.edge("Fill Date","Fill Category")
    graph.edge("Fill Category","Fill Description")
    graph.edge("Fill Description","Fill Amount")
    graph.edge("Fill Amount","Click Add Expense button")
    graph.edge("Click Add Expense button","Click Clear button")
    graph.edge("Click Clear button","Fill Date")

    graph.edge("Click View Expense tab","Fill From Date")
    graph.edge("Fill From Date","Fill To Date")
    graph.edge("Fill To Date","Choose Minimum value for the amount")
    graph.edge("Choose Minimum value for the amount","Choose Maximum value for the amount")
    graph.edge("Choose Maximum value for the amount","Choose Categories")
    graph.edge("Choose Categories","You will get a visual report.")

    graph.edge("Click Analysis tab.","You will get the detailed report.")
    st.graphviz_chart(graph,use_container_width=True)