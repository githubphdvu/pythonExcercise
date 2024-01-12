def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.
    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)
    Return results of conversion, if any.
    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]"
    For example:
      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    if unit_in != "f" and unit_in != "c": return f"Invalid unit {unit_in}"
    if unit_out != "c" and unit_out != "f": return f"Invalid unit {unit_out}"
    if unit_in == "f" and unit_out == "c": temp = (temp - 32) / 9 * 5
    if unit_in == "c" and unit_out == "f": temp = (temp * 5 / 9) + 32
    return temp    

print("c", "f", 0, convert_temp("c", "f", 0), "Result is: 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "Result is: 100.0")
print("ABC", "f", 32, convert_temp("ABC", "f", 32), "Result is: Invalid unit ABC")
print("c", "123", 32, convert_temp("c", "123", 32), "Result is: Invalid unit 123")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "Result is: 75.5")
print("c", "c", 75.5, convert_temp("c", "c", 75.5), "Result is: 75.5")

