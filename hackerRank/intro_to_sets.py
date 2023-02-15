def average(array):
    plant_heights = [int(i) for i in array]

    set_of_plant_heights = set(plant_heights)

    average = sum(set_of_plant_heights)/len(set_of_plant_heights)

    return average

if __name__ == '__main__':
    size_of_array = int(input())
    plant_heights = list(input().split())

    print(average(plant_heights))