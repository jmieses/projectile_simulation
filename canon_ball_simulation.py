# canon_ball_simulation.py

from Projectile import Projectile


def get_inputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initil height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def main():
    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))


if __name__ == '__main__':
    main()