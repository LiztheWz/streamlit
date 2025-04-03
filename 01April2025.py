import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title('My Name App')

# read in data
names = pd.read_csv('all_names.csv')

# pick a name
name_interest = st.text_input('Enter a name')
sex_interest = st.radio('Choose the sex to plot', ['M', 'F'])
# plot_female = st.checkbox('Plot female line')
# plot_female = st.checkbox('Plot male line')
names_df = names[(names['name'] == name_interest) & (names['sex'] == sex_interest)]
names_df.head()


# create plot
fig = plt.figure(figsize=(10,5))
sns.lineplot(x=names_df['year'], y=names_df['count'])
plt.title(f'Plot of {name_interest}')
plt.xlabel('year')
plt.ylabel('count')
plt.xticks(rotation=90)
plt.show()

st.pyplot(fig)

