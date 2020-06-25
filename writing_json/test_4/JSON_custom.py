import json

def complex_encoder(z):
    if isinstance(z,complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type {type_name} si not \JSON serializable")

json_str = json.dumps( 4+6j, default=complex_encoder)
print(json_str)
