from textwrap import dedent

class QUESTION1_PROMPT:

    prompt = dedent('''
                    Your task is to look at the following Patient Blood Pressure, Observation Date, Observation Result, Observation Units, 
                    and determine if the patient have Hypertension/Hypotension.

                    {reference}

                    This is part of an automated evaluation process, therefore you must only output a single word: "Hypertension ", "Hypotension" or "Normal"
    '''
    ).strip()

class QUESTION2_PROMPT:

    prompt = dedent('''
                    Your task is to look at the following Patient	MedInterval, OrderStartDate, Description, Amount, Units, DosageForm, ProviderInstructions, 
                    and determine if the patient get the medication order to treat hypertension/hypotension if any?

                    {reference}

                    This is part of an automated evaluation process, therefore you must only output a single word: "Yes" or "No"
    '''
    ).strip()