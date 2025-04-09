import matplotlib.pyplot as plt
import seaborn as sns

# Données simulées
data = {
    'commandes': 500,
    'commandes_livrees_a_temps': 420,
    'stock_moyen': 120000,  # en €
    'ventes_net': 600000,   # en €
    'cout_biens_vendus': 450000,
    'taux_possession': 0.25,
    'commandes_parfaites': 385,
    'cout_total_transport': 75000,  # en €
    'tonnage_total': 1500,  # en tonnes
    'delais_livraisons_fournisseurs': [True, True, False, True, False, True, True, True, False, True],
}

# 1. Calcul des KPI
kpi = {}

# Ponctualité des livraisons clients
kpi['Ponctualité client (%)'] = (data['commandes_livrees_a_temps'] / data['commandes']) * 100

# Ratio Stock / Ventes
kpi['ISR (Stock/Ventes)'] = data['stock_moyen'] / data['ventes_net']

# Coût de possession du stock
kpi['Coût de possession (€)'] = data['stock_moyen'] * data['taux_possession']

# Ponctualité des livraisons fournisseurs
kpi['Ponctualité fournisseurs (%)'] = (sum(data['delais_livraisons_fournisseurs']) / len(data['delais_livraisons_fournisseurs'])) * 100

# DSI – Durée moyenne de rotation des stocks
kpi['DSI (jours)'] = (data['stock_moyen'] / data['cout_biens_vendus']) * 365

# Coût de transport par tonne
kpi['Coût transport/tonne (€)'] = data['cout_total_transport'] / data['tonnage_total']

# Taux de commandes parfaites
kpi['Taux de commandes parfaites (%)'] = (data['commandes_parfaites'] / data['commandes']) * 100

# Affichage des résultats
print("🔍 Résultats des KPI logistiques :\n")
for key, value in kpi.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")

# 2. Visualisation avec Seaborn
sns.set(style="whitegrid")

# Barplot des KPI %
kpi_pourcentage = {k: v for k, v in kpi.items() if "(%)" in k}
plt.figure(figsize=(10, 6))
sns.barplot(x=list(kpi_pourcentage.values()), y=list(kpi_pourcentage.keys()), palette="viridis")
plt.title("📊 KPI Supply Chain – Taux (%)")
plt.xlabel("Pourcentage (%)")
plt.tight_layout()
plt.show()

# Barplot autres KPI numériques
kpi_valeurs = {k: v for k, v in kpi.items() if "(%)" not in k}
plt.figure(figsize=(10, 6))
sns.barplot(x=list(kpi_valeurs.values()), y=list(kpi_valeurs.keys()), palette="mako")
plt.title("📦 KPI Supply Chain – Valeurs")
plt.xlabel("Valeur (€ ou jours)")
plt.tight_layout()
plt.show()

# 3. Recommandations simples
print("\n💡 Recommandations stratégiques :\n")

if kpi['Ponctualité client (%)'] < 90:
    print("- Améliorer la ponctualité des livraisons clients (actuellement à {:.2f}%).".format(kpi['Ponctualité client (%)']))

if kpi['ISR (Stock/Ventes)'] > 0.25:
    print("- Réduire le stock moyen ou augmenter les ventes pour améliorer le ratio ISR (actuellement à {:.2f}).".format(kpi['ISR (Stock/Ventes)']))

if kpi['Ponctualité fournisseurs (%)'] < 90:
    print("- Renégocier les délais ou changer de fournisseurs peu fiables (ponctualité actuelle : {:.2f}%).".format(kpi['Ponctualité fournisseurs (%)']))

if kpi['Taux de commandes parfaites (%)'] < 95:
    print("- Mettre en place un contrôle qualité ou fiabiliser le process logistique (actuellement {:.2f}%).".format(kpi['Taux de commandes parfaites (%)']))

if kpi['DSI (jours)'] > 90:
    print("- Réduire la durée moyenne de stockage pour améliorer la rotation (DSI = {:.2f} jours).".format(kpi['DSI (jours)']))
