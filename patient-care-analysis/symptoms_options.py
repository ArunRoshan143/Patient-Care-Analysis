unique_symptoms = [
    'itching, skin rash, nodal skin eruptions',
    'skin rash, nodal skin eruptions, dischromic patches',
    'itching, nodal skin eruptions, dischromic patches',
    'itching, skin rash, dischromic patches',
    'continuous sneezing, shivering, chills',
    'shivering, chills, watering from eyes',
    'continuous sneezing, chills, watering from eyes',
    'continuous sneezing, shivering, watering from eyes',
    'stomach pain, acidity, ulcers on tongue',
    'stomach pain, ulcers on tongue, vomiting',
    'stomach pain, acidity, vomiting',
    'acidity, ulcers on tongue, vomiting',
    'itching, vomiting, yellowish skin',
    'vomiting, yellowish skin, nausea',
    'itching, yellowish skin, nausea',
    'itching, vomiting, nausea',
    'itching, skin rash, stomach pain',
    'itching, stomach pain, burning micturition',
    'itching, skin rash, burning micturition',
    'skin rash, stomach pain, burning micturition',
    'vomiting, loss of appetite, abdominal pain',
    'vomiting, indigestion, abdominal pain',
    'indigestion, loss of appetite, abdominal pain',
    'vomiting, indigestion, loss of appetite',
    'vomiting, sunken eyes, dehydration',
    'sunken eyes, dehydration, diarrhoea',
    'vomiting, dehydration, diarrhoea',
    'vomiting, sunken eyes, diarrhoea',
    'fatigue, cough, high fever',
    'cough, high fever, breathlessness',
    'fatigue, high fever, breathlessness',
    'fatigue, cough, breathlessness',
    'acidity, indigestion, headache',
    'indigestion, headache, blurred and distorted vision',
    'acidity, headache, blurred and distorted vision',
    'acidity, indigestion, blurred and distorted vision',
    'back pain, weakness in limbs, neck pain',
    'weakness in limbs, neck pain, dizziness',
    'back pain, neck pain, dizziness',
    'back pain, weakness in limbs, dizziness',
    'vomiting, headache, weakness of one body side',
    'headache, weakness of one body side, altered sensorium',
    'vomiting, weakness of one body side, altered sensorium',
    'vomiting, headache, altered sensorium',
    'itching, vomiting, fatigue',
    'itching, fatigue, weight loss',
    'itching, vomiting, weight loss',
    'chills, vomiting, high fever',
    'vomiting, high fever, sweating',
    'chills, high fever, sweating',
    'chills, vomiting, sweating',
    'itching, skin rash, fatigue',
    'skin rash, fatigue, lethargy',
    'itching, skin rash, lethargy',
    'skin rash, chills, joint pain',
    'chills, joint pain, vomiting',
    'skin rash, joint pain, vomiting',
    'skin rash, chills, vomiting',
    'chills, vomiting, fatigue',
    'joint pain, vomiting, yellowish skin',
    'vomiting, yellowish skin, dark urine',
    'joint pain, yellowish skin, dark urine',
    'joint pain, vomiting, dark urine',
    'itching, fatigue, lethargy',
    'fatigue, lethargy, yellowish skin',
    'itching, lethargy, yellowish skin',
    'itching, fatigue, yellowish skin',
    'fatigue, yellowish skin, nausea',
    'yellowish skin, nausea, loss of appetite',
    'fatigue, nausea, loss of appetite',
    'fatigue, yellowish skin, loss of appetite',
    'joint pain, vomiting, fatigue',
    'vomiting, fatigue, yellowish skin',
    'joint pain, fatigue, yellowish skin',
    'joint pain, vomiting, fatigue',
    'vomiting, fatigue, high fever',
    'joint pain, fatigue, high fever',
    'joint pain, vomiting, high fever',
    'vomiting, yellowish skin, abdominal pain',
    'yellowish skin, abdominal pain, swelling of stomach',
    'vomiting, abdominal pain, swelling of stomach',
    'vomiting, yellowish skin, swelling of stomach',
    'chills, vomiting, fatigue',
    'chills, fatigue, weight loss',
    'chills, vomiting, weight loss',
    'continuous sneezing, chills, fatigue',
    'chills, fatigue, cough',
    'continuous sneezing, fatigue, cough',
    'continuous sneezing, chills, cough',
    'chills, fatigue, cough',
    'fatigue, cough, high fever',
    'chills, cough, high fever',
    'constipation, pain during bowel movements, pain in anal region',
    'pain during bowel movements, pain in anal region, bloody stool',
    'constipation, pain in anal region, bloody stool',
    'constipation, pain during bowel movements, bloody stool',
    'vomiting, breathlessness, sweating',
    'breathlessness, sweating, chest pain',
    'vomiting, sweating, chest pain',
    'vomiting, breathlessness, chest pain',
    'fatigue, cramps, bruising',
    'cramps, bruising, obesity',
    'fatigue, bruising, obesity',
    'fatigue, cramps, obesity',
    'fatigue, weight gain, cold hands and feet',
    'weight gain, cold hands and feet, mood swings',
    'fatigue, cold hands and feet, mood swings',
    'fatigue, weight gain, mood swings',
    'fatigue, mood swings, weight loss',
    'mood swings, weight loss, restlessness',
    'fatigue, weight loss, restlessness',
    'fatigue, mood swings, restlessness',
    'vomiting, fatigue, anxiety',
    'fatigue, anxiety, sweating',
    'vomiting, anxiety, sweating',
    'vomiting, fatigue, sweating',
    'joint pain, neck pain, knee pain',
    'neck pain, knee pain, hip joint pain',
    'joint pain, knee pain, hip joint pain',
    'joint pain, neck pain, hip joint pain',
    'muscle weakness, stiff neck, swelling joints',
    'stiff neck, swelling joints, movement stiffness',
    'muscle weakness, swelling joints, movement stiffness',
    'muscle weakness, stiff neck, movement stiffness',
    'vomiting, headache, nausea',
    'headache, nausea, spinning movements',
    'vomiting, nausea, spinning movements',
    'vomiting, headache, spinning movements',
    'skin rash, pus filled pimples, blackheads',
    'pus filled pimples, blackheads, scarring',
    'skin rash, blackheads, scarring',
    'skin rash, pus filled pimples, scarring',
    'burning micturition, bladder discomfort, foul smell of urine',
    'bladder discomfort, foul smell of urine, continuous feel of urine',
    'burning micturition, foul smell of urine, continuous feel of urine',
    'burning micturition, bladder discomfort, continuous feel of urine',
    'skin rash, joint pain, skin peeling',
    'joint pain, skin peeling, silver like dusting',
    'skin rash, skin peeling, silver like dusting',
    'skin rash, joint pain, silver like dusting',
    'skin rash, high fever, blister',
    'high fever, blister, red sore around nose',
    'skin rash, blister, red sore around nose',
    'skin rash, high fever, red sore around nose'
]