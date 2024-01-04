#!/usr/local/bin/python3
# route.py : Find routes through maps
#
# Code by: ashvenk-zeepatel-vekal-dfranci
#
# Based on skeleton code by B551 Course Staff, Fall 2023
#


# !/usr/bin/env python3
import heapq
import sys
import math

def build_graph():
    graph = {}
    city_coordinates = {}

    # Read data from 'city-gps.txt' and build city_coordinates
    with open('city-gps.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(' ')
            city = parts[0]
            lat, lon = map(float, parts[1:])
            city_coordinates[city] = (lat, lon)

    with open('road-segments.txt', 'r') as f:
        for line in f:
            city_1, city_2, road_length, speed_limit, road_name = line.strip().split(' ')
            road_length, speed_limit = float(road_length), float(speed_limit)
            
            if city_1 not in graph:
                graph[city_1] = {}
            if city_2 not in graph:
                graph[city_2] = {}

            # Calculate the delivery_time based on speed_limit and road length
            if speed_limit >= 50:
                # Calculate probability of a mistake
                probability = math.tanh(road_length / 1000)
                # Calculate additional time for delivery
                delivery_time = (road_length / speed_limit) + probability * 2 * (road_length / speed_limit)
            else:
                delivery_time = road_length / speed_limit

            segment_info = {
                'distance': road_length,
                'speed_limit': speed_limit,
                'segment_info': road_name,
                'time': road_length / speed_limit,
                'delivery_time': delivery_time
            }

            graph[city_1][city_2] = segment_info
            graph[city_2][city_1] = segment_info

    return graph, city_coordinates

def calculate_cost(segment_info, cost):
    if cost == 'segments':
        return 1
    elif cost == 'distance':
        return segment_info['distance']
    elif cost == 'time':
        return segment_info['time']
    elif cost == 'delivery':
        return segment_info['delivery_time']

def get_route(start, end, cost):
    graph, city_coordinates = build_graph()

    # heuristic function for A*
    def heuristic(city1, city2):
        x1, y1 = city_coordinates.get(city1, (0, 0))  
        x2, y2 = city_coordinates.get(city2, (0, 0))  
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.009

    # open set, closed set, and a dictionary to store parent cities and their costs
    open_set = [(0, start)]  # f-value, city
    closed_set = set()
    parent = {start: (None, None, 0)}  # parent city, segment info, and cost

    route_taken = []
    total_segments = 0
    total_miles = 0.0
    total_hours = 0.0
    total_delivery_hours = 0.0

    # A* algorithm to find the route
    while open_set:
        # Get the city with the lowest f-value from the open set
        f, current_city = heapq.heappop(open_set)

        if current_city == end:
            while current_city in parent:
                next_city, segment_info, segment_cost = parent[current_city]
                if next_city is not None:
                    route_taken.insert(0, (current_city, segment_info))
                    total_segments += 1
                    total_miles += graph[current_city][next_city]['distance']
                    total_hours += graph[current_city][next_city]['time']
                    total_delivery_hours += graph[current_city][next_city]['delivery_time']
                current_city = next_city
            return {
                "route-taken": route_taken,
                "total-segments": total_segments,
                "total-miles": total_miles,
                "total-hours": total_hours,
                "total-delivery-hours": total_delivery_hours
            }

        closed_set.add(current_city)

        for neighbor, segment_info in graph[current_city].items():
            if neighbor not in closed_set:
                g = parent[current_city][2] + calculate_cost(segment_info, cost)
                h = heuristic(neighbor, end)
                f = g + h
                heapq.heappush(open_set, (f, neighbor))
                if neighbor not in parent or g < parent[neighbor][2]:
                    parent[neighbor] = (current_city, segment_info['segment_info'], g)
    return None

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