def rule_check(symptoms, age):
    s = symptoms.lower()
    if "chest pain" in s and "breath" in s:
        return "Emergency", "Critical cardiac symptoms"
    if age < 5 and "fever" in s:
        return "High", "Pediatric fever"
    return None
