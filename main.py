# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, template="Hello, <name>!"):
    result = template.replace('<name>', name)
    return result

def force(mass, body='earth'):
    gravity_dict = {
        "mercury": 3.7,
        "venus": 8.9,
        "earth": 9.8,
        "mars": 3.7,
        "jupiter": 24.9,
        "saturn": 10.4,
        "neptune": 11.2,
        "sun": 274,
        "moon": 1.6,
        "pluto": 0.6
    }
    return mass * gravity_dict[body]

def pull(m1, m2, d):
    G = 0.00000000006674
    return G* ((m1*m2)/d**2)

