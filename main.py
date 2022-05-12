# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):
    greeting = greeting.replace("<name>", name)
    return greeting


def force(mass, body='earth'):
    gravity = {
        "earth": 9.8,
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "uranus": 8.87,
        "venus": 8.87,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58
    }
    gravity = round(gravity[body], 1)
    force = mass * gravity
    return force


def pull(m1, m2, d):
    g = 6.674 * 10 ** -11
    pull = g * ((m1 * m2) / (d**2))
    return pull


if __name__ == "__main__":
    greet("Bob")
    force(80)
    pull(800, 1500, 3)
