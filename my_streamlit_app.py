import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Ceci est une étude de corrélation sur les voitures')

st.write("Commencons par regarder différents graphiques...")
st.write("mpg = miles par gallon = Consommation du carburant")
st.write("cylinders = Nombre de cylindres, entre 4-8")
st.write("hp = Nombre de cylindres, entre 4-8")
st.write("weightslbs = poids du véhicule")
st.write("time-to-60 = Temps d'accélation")
st.write("year = année du modèle")


lien = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(lien)

st.header("Voici la heatmap des corrélations...")
## graph correlation
viz_correlation = plt.figure(figsize=(6,6))
viz_correlation = sns.heatmap(df.corr(),
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
								annot=True
								)
st.pyplot(viz_correlation.figure)

### Graph du nombre 
st.subheader("Production de voiture par continent")

count_plot = plt.figure()
count_plot = sns.countplot(x='year',hue='continent',data=df)
st.pyplot(count_plot.figure)


### Choisir un pays : Bouton
st.subheader('Et si on zoomait par continent ?')

select_continent = st.multiselect("Choississez un continent:", df["continent"].unique(), )
select_continent

### df_filtré
df_filtre = df[df["continent"].isin(select_continent)]
df_filtre

### nombre de voiture par continent dans le jeu de données
continent = df_filtre["continent"]
st.write("**Nombre de voiture dans la sélection:**", continent.count())

### indicateurs de moyenne
st.subheader('Quelques moyennes')

moy_l_filtre = round(df_filtre["mpg"].mean(),2)
moy_weights_filtre= round(df_filtre["weightlbs"].mean(),2)
moy_annee= round(df_filtre["year"].mean(),2)

col1, col2, col3 = st.columns(3)
col1.metric("Moyenne de consommation", moy_l_filtre)
col2.metric("Moyenne du poids des véhicules", moy_weights_filtre)
col3.metric("Année moyenne de sortie des véhicules",moy_annee )

### etude sur cylindres et poids
st.title("Est ce que le nombre de cylindres influe sur le poids du vehicule ?")
fig1 = plt.figure()
fig1 = sns.scatterplot(data= df_filtre , x = 'cylinders', y='weightlbs', color = "darkred")                                           
st.pyplot(fig1.figure)
st.write("Oui, le tout est corrélé, plus il y a de cylindres, plus le véhicule est lourd")

### ajout d'indcateurs sur la sélection
annee_creation = df_filtre["year"].min()
time= round(df_filtre["time-to-60"].mean(),2)

col1, col2 = st.columns(2)
col1.metric("La 1er voiture fut créée en ", annee_creation)
col2.metric("Moyenne d'accélération", time)

### Bar plot, evolution du poids des voitures selon les années de création 
fig2 = plt.figure()
fig2 = sns.barplot(data= df_filtre , x = 'year', y= 'weightlbs')                                           
st.pyplot(fig2.figure)





