from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Define input model
class RomanNumber(BaseModel):
    roman_numeral: str

# Conversion function
def roman_to_int(roman: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_prev_char = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
    result = 0
    prev_value = float("inf")
    prev_prev_value = prev_value
    prev_char = None
    
    try:
        if "VV" in roman or "LL" in roman or "DD" in roman:
            raise ValueError
        for i in range(len(roman)):
            i_prev = i - 1 if i != 0 else None
            i_next = i + 1 if i != len(roman) - 1 else None
            char = roman[i]
            current_value = roman_values[char]
            if current_value > prev_value:
                if i_prev is not None:
                    prev_char = roman[i_prev]
                    if prev_char != roman_prev_char[char]:
                        raise ValueError
                    result -= prev_value
                    current_value -= prev_value
                    if current_value > prev_prev_value:
                        raise ValueError
                    result += current_value
                    if i_next is not None:
                        next_char = roman[i_next]
                        if next_char == prev_char:
                            raise ValueError
            else:
                result += current_value
            prev_prev_value = prev_value
            prev_value = current_value
            prev_char = char
    except (KeyError, ValueError):
        raise Exception("Invalid Roman numeral")
    
    return result
    
# Define the API
@app.post("/convert/")
async def convert_roman_to_integer(input_data: RomanNumber):
    roman_numeral = input_data.roman_numeral.upper()

    # Validate Roman numeral (characters and length)
    if not all(c in 'IVXLCDM' for c in roman_numeral) or not (1 <= len(roman_numeral) <= 15):
        raise HTTPException(status_code=400, detail="Invalid Roman numeral format")
    
    try:
        integer_value = roman_to_int(roman_numeral)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"integer_value": integer_value}
