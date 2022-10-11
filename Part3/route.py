#!/usr/local/bin/python3
# route.py : Find routes through maps
#
# Code by: VNAYAKAN, TMAHIND, DBRAJ
#
# Based on skeleton code by V. Mathur and D. Crandall, Fall 2022
#


# !/usr/bin/env python3
import sys
import math
import heapq as hp

# Function implementing Haversine formula to find the heuristic distance from source to destination.
def haversine_distance(city1, city2):
    radius_in_miles = 3963
    latitude1, longitude1 = math.radians(float(city1[0])), math.radians(float(city1[1]))
    latitude2, longitude2 = math.radians(float(city2[0])), math.radians(float(city2[1]))
    latitude_diff = latitude1 - latitude2
    longitude_diff = longitude1 - longitude2
    squared_num = (math.sin(latitude_diff/2)**2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(longitude_diff/2)**2)
    distance = 2 * radius_in_miles * math.asin(math.sqrt(squared_num))
    return distance


# A simple function to find successors.
def successors(road_segments, current_city):
    return road_segments[current_city]


# This function calculates h(s), and returns f(s) where f(s) = g(s) + h(s) for all cost functions.
def heuristic(city_gps, end, city_data, fringe, cost):
    if cost == 'delivery':
        if fringe[0] in city_gps:
            return_val = city_data[4] + float(fringe[1]) / float(fringe[2]) + \
                   haversine_distance(city_gps[fringe[0]], city_gps[end]) / 49
            if float(fringe[2]) >= 50:
                return_val += 2 * (city_data[4] + float(fringe[1]) / float(fringe[2])) * math.tanh(float(fringe[1])/1000)
            return return_val
        else:
            return_val = float(fringe[1]) / float(fringe[2]) + city_data[4]
            if float(fringe[2]) >= 50:
                return_val += 2 * (city_data[4] + float(fringe[1]) / float(fringe[2])) * math.tanh(float(fringe[1])/1000)
            return return_val
        

    elif cost == 'distance':
        if fringe[0] in city_gps:
            return city_data[2] + float(fringe[1]) + haversine_distance(city_gps[fringe[0]], city_gps[end])
        else:
            return city_data[2] + float(fringe[1])
    # In this cost function, I'm dividing the heuristic distance by 49 since that's the maximum possible speed limit
    # for which the delivery driver will not have a probability of dropping the package.
    elif cost == 'segments':
        return city_data[1] + 1
    # In this cost function, I'm dividing the heuristic distance by 50 where 50 is an observed median speed limit for
    # all highways.
    elif cost == 'time':
        if fringe[0] in city_gps:
            return city_data[3] + float(fringe[1]) / float(fringe[2]) + \
                   haversine_distance(city_gps[fringe[0]], city_gps[end]) / 50
        else:
            return city_data[3] + float(fringe[1]) / float(fringe[2])

    


def get_route(start, end, cost):

    # Each item in city_gps dictionary has the format - { city_name: [latitude, longitude] }.
    city_gps = {}
    with open('./city-gps.txt', 'r') as file:
        city_gps = {line.split()[0]:line.split()[1:] for line in file}
    road_segments = {}
    # Each item in road_segments dictionary has the format - { city1: [[city2, distance, speed_limit, highway_name]] }.
    
    # All the city names, be it city1 or city2 in each line of road-segments.txt, will be a key in road_segments
    # dictionary. In this way, we can directly find the roads leading out of any city we are currently in.
    with open('./road-segments.txt', 'r') as file:
        for line in file:
            line_list = line.split()
            if line_list[1] not in road_segments:
                road_segments[line_list[1]] = [line_list[:1] + line_list[2:]]  
            else:
                road_segments[line_list[1]].append(line_list[:1] + line_list[2:])
            if line_list[0] not in road_segments:
                road_segments[line_list[0]] = [line_list[1:]]
            else:
                road_segments[line_list[0]].append(line_list[1:])
    return evaluation(start, end, city_gps, road_segments, cost)


def evaluation(start, end, city_gps, road_segments, cost):
    fringe = []
    # each node in the heap/ fringe has the following
    # DUMMY HEURISTIC(current_city, segments, distance, time, delivery_hours, route_taken).
    fringe.append((1, (start, 0, 0, 0, 0, [])))
    hp.heapify(fringe)
    while len(fringe)>0:
        _, city_data = hp.heappop(fringe)
        for s in successors(road_segments, city_data[0]):
            hp.heappush(fringe,(heuristic(city_gps, end, city_data, s, cost), (s[0], city_data[1] + 1, city_data[2] + float(s[1]), city_data[3] + float(s[1]) / float(s[2]), city_data[4] + float(s[1]) / float(s[2])\
                + 2 * (city_data[4] + float(s[1]) / float(s[2])) * math.tanh(float(s[1])/1000) if float(s[2]) >= 50 else city_data[4] + float(s[1]) / float(s[2]), city_data[5] + [(s[0], s[3] + ' for ' + s[1] + ' miles')])))
        if city_data[0] == end:
            return {"total-segments": city_data[1],
                    "total-miles": city_data[2],
                    "total-hours": city_data[3],
                    "total-delivery-hours": city_data[4],
                    "route-taken": city_data[5]}


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise(Exception("Error: expected 3 arguments"))

    (_, start_city, end_city, cost_function) = sys.argv
    if cost_function not in ("segments", "distance", "time", "delivery"):
        raise(Exception("Error: invalid cost function"))

    result = get_route(start_city, end_city, cost_function)

    # Pretty print the route
    print("Start in %s" % start_city)
    for step in result["route-taken"]:
        print("   Then go to %s via %s" % step)

    print("\n          Total segments: %4d" % result["total-segments"])
    print("             Total miles: %8.3f" % result["total-miles"])
    print("             Total hours: %8.3f" % result["total-hours"])
    print("Total hours for delivery: %8.3f" % result["total-delivery-hours"])


