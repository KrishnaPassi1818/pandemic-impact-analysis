class Predictor:
    def predict_risk(self, data):
        results = []

        for _, row in data.iterrows():
            if row['cases_per_million'] > 50000 or row['death_rate'] > 2:
                risk = "High"
            elif row['cases_per_million'] > 10000:
                risk = "Medium"
            else:
                risk = "Low"

            results.append({
                "Country": row['location'],
                "Risk Level": risk,
                "Cases/Million": round(row['cases_per_million'], 2),
                "Death Rate (%)": round(row['death_rate'], 2)
            })

        return results[:10]  # show top 10 only