# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:23:08 2023

@author: GALVJ
"""

import streamlit as st
from PIL import Image

st.title('Data Quality Spotlight: Accuracy')
st.caption('10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com')

col11,col22 = st.columns([3,1])
with col11:
    title_img = Image.open("phone numbers title.png")
    st.image(title_img)
st.text('Have you ever stopped to appreciate the extraordinary feat of data governance that \n'
        'goes into assigning telephone numbers? Each number can be assigned to one-and-only-\n'
        'one person in the world. Each country has its own allowable number of digits and an \n'
        'accepted format. And there is universal acceptance of this system! Verizon never \n'
        'just decides to start assigning 20-digit phone numbers to its customers.')
st.text('Nope. There is a string of 10 digits that is universally accepted as MY phone \n'
        'number, just as there is a string of 10 digits that is universally accepted as \n'
        'YOUR phone number.')
col1, col2 = st.columns(2)

with col1:
    and_yet_img = Image.open('and yet.jpg')
    st.image(and_yet_img)
st.text("You haven't fully lived until you've either heard or spoken the phrase,")

sorry_img = Image.open('sorry wrong number.png')
st.image(sorry_img)

col3,col4 = st.columns([3,1])

with col3:
    st.text("So, what gives? Two dynamics are at play. First, we have the \n"
            "people who intentionally spread fake news. Second, we have the \n"
            "accidental fake news spreaders, made possible because a\n"
            "person is copying a phone number, rather than pulling it\n"
            "directly from a system of record.")
    with st.expander("System of Record? 🤔"):
        sor_img = Image.open("sor.png")
        st.image(sor_img)
    st.text('In the phone number context, a system of record is less \n'
            'important for our intentional fake-newsers because\n'
            "if someone doesn't want us to have their phone number,\n"
            "we should probably just move on.")
with col4:
    fig1_img= Image.open('fig1.png')
    st.image(fig1_img)
    
st.text("But the second dynamic illustrates why designating a system of record for critical\n"
        "data is so important.")
st.text("Consider for a moment if there were no national telephone registry.")
st.text("Phone numbers don't occur naturally. They aren't something we're born with. They\n"
        "aren't immutably attached to anything in the physical environment.")
st.text("Now, contrast this to something like eye color. \nI don't care what any database says:")
col44,col45,col46 = st.columns([.5,3,.5])
with col45:
    eyes_img = Image.open('green eyes.png')
    st.image(eyes_img)
st.text("You can look at me and verify this statement. But without a designated, universally-\naccepted national telephone registry, things would be chaos!")


st.text("Multiple people could have the same number!")
st.text("First responders wouldn't be able to trace calls!")
st.text("We'd probably have 20-digit numbers because we wouldn't know if a number \ncould be reused!") 
st.text("Fake news would proliferate!!")
st.text("In other words, we can ensure the accuracy of data by comparing it to its\nsystem of record."
        " Ultimately, this greatly improves the useability of the data.")
with st.expander("Accuracy? 🤔"):
    col66,col67 = st.columns(2)
    with col66:
        acc_img = Image.open("accuracy.png")
        st.image(acc_img)
    with col67:
        tree_img = Image.open("trees.png")
        st.image(tree_img)

col7,col8 = st.columns([3,3])
with col7:
    st.subheader("Let's do a knowledge check")
    st.text('Which data needs a system of record?')
    think_img = Image.open('think_fig.png')
    st.image(think_img)
with col8:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    logon = st.checkbox('Employee Logon IDs')
    if logon:
        st.text('Absolutely!')
    hair = st.checkbox('Hair color')
    if hair:
        st.text("Probably not. If we did track hair color \nin databases and needed to check entries \nfor accuracy, we could probably just look \nat people's heads.")
    salary = st.checkbox('Employee salary data')
    if salary:
        st.text("For sure.")
    phone = st.checkbox('Phone numbers')
    if phone:
        st.text("Of course! I would be quite sad if I \nhadn't convinced you of that.")
    
st.subheader("Fight Fake News With Us")
st.text("Have you heard that we're building out a data catalog? As part of our data\n"
        "governance program, we work across the firm to designate systems of record for our \n"
        "most important data. With our data catalog, Collibra, you can browse and search\n"
        "for data, along with their systems of record.")
col9,col10 = st.columns(2)
with col9:
    st.text("We add new data all the time, so check it\nout and help"
            " us end fake news once and\nfor all!"
            '\n\nTo learn more and get involved, reach out\nto Jordan Galvin'
            ' at\nDataGovernance@perkinscoie.com')
with col10:
    high_five_img = Image.open("high five.png")
    st.image(high_five_img)