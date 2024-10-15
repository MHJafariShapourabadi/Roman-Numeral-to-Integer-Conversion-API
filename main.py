from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Define input model
class RomanNumber(BaseModel):
    roman_numeral: str

# Conversion function
def roman_to_int(roman: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_prev_char = {'I': 'I', 'V': 'I', 'X': 'IX', 'L': 'X', 'C': 'XC', 'D': 'C', 'M': 'CM'}
    result = 0
    prev_value = 0
    prev_char = None
    
    try:
        for char in reversed(roman):
            current_value = roman_values[char]
            if current_value <= prev_value and char not in roman_prev_char[prev_char]:
                raise ValueError
            if current_value < prev_value:
                result -= current_value
                current_value = prev_value - current_value
            else:
                result += current_value
            prev_value = current_value
            prev_char = char
    except (KeyError, ValueError):
        raise HTTPException(status_code=400, detail="Invalid Roman numeral")
    
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
