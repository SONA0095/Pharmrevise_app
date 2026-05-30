from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# ================= ROOT ROUTE =================
@app.route("/")
def home():
    return jsonify({
        "message": "PharmReVise API is running 🚀",
        "available_endpoints": "/api/..."
    })


# ================= DRUG-TARGET DOCKING =================
@app.route('/api/drug-target-docking', methods=['POST'])
def drug_target_docking():
    data = request.json
    drug_name = data.get("Drug Name")
    target_protein = data.get("Target Protein")
    docking_score = round(random.uniform(-10, 0), 2)
    return jsonify({
        "Drug Name": drug_name,
        "Target Protein": target_protein,
        "Docking Score": docking_score
    })


# ================= BINDING AFFINITY =================
@app.route('/api/binding-affinity-prediction', methods=['POST'])
def binding_affinity():
    data = request.json
    drug_name = data.get("Drug Name")
    target_protein = data.get("Target Protein")
    affinity_score = round(random.uniform(-12, 0), 2)
    return jsonify({
        "Drug Name": drug_name,
        "Target Protein": target_protein,
        "Binding Affinity": affinity_score
    })


# ================= TARGET IDENTIFICATION =================
@app.route('/api/ai-powered-target-identification', methods=['POST'])
def ai_target_identification():
    data = request.json
    disease_name = data.get("Disease Name")
    predicted_targets = ["TargetA", "TargetB", "TargetC"]
    return jsonify({
        "Disease Name": disease_name,
        "Predicted Targets": predicted_targets
    })


# ================= MOLECULAR SIMILARITY =================
@app.route('/api/molecular-similarity-search', methods=['POST'])
def molecular_similarity():
    data = request.json
    drug_name = data.get("Drug Name")
    similar_drugs = ["DrugX", "DrugY", "DrugZ"]
    return jsonify({
        "Drug Name": drug_name,
        "Similar Drugs": similar_drugs
    })


# ================= PATHWAY ANALYSIS =================
@app.route('/api/pathway-mechanism-analysis', methods=['POST'])
def pathway_analysis():
    data = request.json
    drug_name = data.get("Drug Name")
    pathways = ["Pathway1", "Pathway2", "Pathway3"]
    return jsonify({
        "Drug Name": drug_name,
        "Associated Pathways": pathways
    })


# ================= ADMET PREDICTION =================
@app.route('/api/admet-prediction', methods=['POST'])
def admet_prediction():
    data = request.json
    drug_name = data.get("Drug Name")

    admet_properties = {
        "Absorption": random.choice(["High", "Medium", "Low"]),
        "Distribution": random.choice(["Extensive", "Limited"]),
        "Metabolism": random.choice(["Hepatic", "Renal", "Both"]),
        "Excretion": random.choice(["Renal", "Biliary", "Both"]),
        "Toxicity": random.choice(["Low", "Medium", "High"])
    }

    return jsonify({
        "Drug Name": drug_name,
        "ADMET Properties": admet_properties
    })


# ================= CLINICAL TRIALS =================
@app.route('/api/clinical-trial-data-lookup', methods=['POST'])
def clinical_trial_lookup():
    data = request.json
    drug_name = data.get("Drug Name")

    trial_data = [
        "Phase I - Completed",
        "Phase II - Ongoing",
        "Phase III - Not Started"
    ]

    return jsonify({
        "Drug Name": drug_name,
        "Clinical Trials": trial_data
    })


# ================= RESEARCH PAPERS =================
@app.route('/api/case-studies-research-papers', methods=['POST'])
def case_studies():
    data = request.json
    drug_name = data.get("Drug Name")

    papers = ["Study A", "Study B", "Study C"]

    return jsonify({
        "Drug Name": drug_name,
        "Research Papers": papers
    })


# ================= DRUG INTERACTION =================
@app.route('/api/drug-drug-interaction-risk', methods=['POST'])
def drug_interaction():
    data = request.json
    drug_name = data.get("Drug Name")
    combination_drug = data.get("Combination Drug")

    interaction_risk = random.choice(["Low", "Moderate", "High"])

    return jsonify({
        "Drug Name": drug_name,
        "Combination Drug": combination_drug,
        "Interaction Risk": interaction_risk
    })


# ================= TOXICITY =================
@app.route('/api/toxicity-side-effect-prediction', methods=['POST'])
def toxicity_prediction():
    data = request.json
    drug_name = data.get("Drug Name")

    side_effects = ["Nausea", "Dizziness", "Liver Damage"]

    return jsonify({
        "Drug Name": drug_name,
        "Predicted Side Effects": side_effects
    })


# ================= FDA STATUS =================
@app.route('/api/fda-approval-status-checker', methods=['POST'])
def fda_approval_status():
    data = request.json
    drug_name = data.get("Drug Name")

    approval_status = random.choice(["Approved", "Pending", "Rejected"])

    return jsonify({
        "Drug Name": drug_name,
        "FDA Approval Status": approval_status
    })


# ================= BRAND INFO =================
@app.route('/api/marketed-brand-lookup', methods=['POST'])
def marketed_by_brand():
    data = request.json
    drug_name = data.get("Drug Name")

    brand_name = f"Brand-{drug_name[:3].upper()}"
    marketed_by = f"PharmaCorp-{drug_name[:3].upper()}"

    return jsonify({
        "Drug Name": drug_name,
        "Brand Name": brand_name,
        "Marketed By": marketed_by
    })


# ================= PATENT DATA =================
@app.route('/api/patent-regulatory-data-search', methods=['POST'])
def patent_regulatory_data():
    data = request.json
    drug_name = data.get("Drug Name")

    patent_status = random.choice(["Active", "Expired", "Pending"])
    regulatory_data = random.choice(["FDA Approved", "Under Review", "Not Approved"])

    return jsonify({
        "Drug Name": drug_name,
        "Patent Status": patent_status,
        "Regulatory Data": regulatory_data
    })


# ================= REPURPOSING SCORE =================
@app.route('/api/repurposing-score', methods=['POST'])
def ai_repurposing_score():
    data = request.json
    drug_name = data.get("Drug Name")

    repurposing_score = round(random.uniform(50, 100), 2)

    return jsonify({
        "Drug Name": drug_name,
        "AI-Powered Repurposing Score": repurposing_score
    })


# ================= RUN APP =================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
