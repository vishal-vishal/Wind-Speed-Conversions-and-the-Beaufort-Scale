#Wind speed conversions and the beaufort scale - www.101computing.net/wind-force/
def check_scal(knot):
    forces = {0: ["Calm", "Sea like a mirror", "Smoke rises vertically"],
              1: ["Light air", "Ripples with appearance of scales are formed, without foam crests",
                  "Direction shown by smoke drift but not by wind vanes."],
              2: ["Light breeze",
                  "Small wavelets still short but more pronounced; crests have a glassy appearance but do not break",
                  "Wind felt on face; leaves rustle; wind vane moved by wind."],
              3: ["Gentle breeze",
                  "Large wavelets; crests begin to break; foam of glassy appearance; perhaps scattered white horses",
                  "Leaves and small twigs in constant motion; light flags extended."],
              4: ["Moderate breeze", "Small waves becoming longer; fairly frequent white horses",
                  "Raises dust and loose paper; small branches moved."],
              5: ["Fresh breeze",
                  "Moderate waves taking a more pronounced long form; many white horses are formed; chance of some spray",
                  "Small trees in leaf begin to sway; crested wavelets form on inland waters."],
              6: ["Strong breeze",
                  "Large waves begin to form; the white foam crests are more extensive everywhere; probably some spray",
                  "Large branches in motion; whistling heard in telegraph wires; umbrellas used with difficulty."],
              7: ["High wind, moderate gale, near gale",
                  "Sea heaps up and white foam from breaking waves begins to be blown in streaks along the direction of the wind; spindrift begins to be seen",
                  "Whole trees in motion; inconvenience felt when walking against the wind."],
              8: ["Gale, fresh gale",
                  "Moderately high waves of greater length; edges of crests break into spindrift; foam is blown in well-marked streaks along the direction of the wind",
                  "Twigs break off trees; generally impedes progress."],
              9: ["Strong/severe gale",
                  "High waves; dense streaks of foam along the direction of the wind; sea begins to roll; spray affects visibility",
                  "Slight structural damage (chimney pots and slates removed)."],
              10: ["Storm, whole gale",
                   "Very high waves with long overhanging crests; resulting foam in great patches is blown in dense white streaks along the direction of the wind; on the whole the surface of the sea takes on a white appearance; rolling of the sea becomes heavy; visibility affected",
                   "Seldom experienced inland; trees uprooted; considerable structural damage."],
              11: ["Violent storm",
                   "Exceptionally high waves; small- and medium-sized ships might be for a long time lost to view behind the waves; sea is covered with long white patches of foam; everywhere the edges of the wave crests are blown into foam; visibility affected",
                   "Very rarely experienced; accompanied by widespread damage."],
              12: ["Hurricane force",
                   "The air is filled with foam and spray; sea is completely white with driving spray; visibility very seriously affected",
                   "Devastation"]
              }
    result = []
    if 0>knot or knot<1:
        result = forces[0]
    elif 1 >= knot or knot <= 3:
        result = forces[1]
    elif 4 >= knot or knot<=6:
        result = forces[2]
    elif 7>= knot or knot <= 10:
        result = forces[3]
    elif 11 >= knot or knot <= 16:
        result = forces[4]
    elif 17 >= knot or knot <= 21:
        result = forces[5]
    elif 22 >= knot or knot <= 27:
        result = forces[6]
    elif 28 >= knot or knot <= 33:
        result = forces[7]
    elif 34 >= knot or knot <= 40:
        result = forces[8]
    elif 41 >= knot or knot <= 47:
        result = forces[9]
    elif 48 >= knot or knot <= 55:
        result = forces[10]
    elif 56 >= knot or knot <= 63:
        result = forces[11]
    else:
        result = forces[12]
    return result


def print_results(result):
    print(f"Wind force : {result[0]}")
    print(f"Description: {result[1]}")
    print(f"Land Condition : {result[2]}")

# Takes User inputs
speed_type = int(input("Please enter a number for\n1 for mph\n2 for km/h\n3 for knot\n: "))
speed = int(input("Enter the speed:"))

#Step 1: Convert this speed in knots knowing that 1 knot = 1.852 km/h
knot = 0
print(speed_type)
if speed_type == 2:
    knot = speed / 1.852
elif speed_type == 3:
    knot = speed
elif speed == 1:
    knot = speed/1.151
print(knot)


#Step 2: Use the Beaufort scale to work out the matching wind force
result = check_scal(knot)

#Step 3: Display the wind force, description, sea conditions and land conditions corresponding to this wind force
print_results(result)


#Step 4: Review the code in step 1 to allow the user to enter the wind speed in the unit of their choice (km/h, mph, knots)