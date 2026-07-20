import glob
import re
count = 0
for filepath in glob.glob("data/templates/*.html"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        continue

    orig = text
    
    # regex substitution
    
    # 1. P31
    text = re.sub(
        r'\?event\s+a\s+base:E5_Event\s*;\s*base:P31_has_modified\s+\$subject\s*;',
        r'$subject base:P31i_was_modified_by ?event . ?event a base:E5_Event ;',
        text
    )
    
    text = re.sub(
        r'\?event\s+a\s+base:E5_Event\s*;\s*base:P31_has_modified\s+\$subject\s*\.',
        r'$subject base:P31i_was_modified_by ?event . ?event a base:E5_Event .',
        text
    )

    # 2. P129 Risk Analysis
    text = re.sub(
        r'base:P2_has_type\s+<https://w3id.org/sirius/risk-analysis>\s*;\s*base:P129_is_about\s+\$subject\s*;',
        r'base:P2_has_type <https://w3id.org/sirius/risk-analysis> . $subject base:P129i_is_subject_of ?riskAnalysis . ?riskAnalysis ',
        text
    )

    # 3. P129 Nara
    text = re.sub(
        r'base:P2_has_type\s+<https://w3id.org/sirius/nara-grid>\s*;\s*base:P129_is_about\s+\$subject\s*;',
        r'base:P2_has_type <https://w3id.org/sirius/nara-grid> . $subject base:P129i_is_subject_of ?analysis . ?analysis ',
        text
    )

    if text != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print("Fixed", filepath)
        count += 1

print(f"Total modified: {count}")
