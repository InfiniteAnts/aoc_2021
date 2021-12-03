import time

"""
Thanks for using Replit for Advent of Code!

Here are a few tips:

1. To install packages, just import them and Replit will install them for you, or click on the cube in the sidebar to install manually.
2. If you're stuck, try using the debugger in the sidebar shaped like a play/pause button.
3. When you're done, you can share your project by clicking the project name and then "Publish"
3.a When you share your project, use the #adventofcode hashtag!
4. Have fun, and good luck!
"""


"""
Place your question data into the data.txt file.
You may need to parse the data!
"""
def part_1():
  with open("data.txt") as f:

    data = f.readlines()

    output = 0
    for i in range(1, len(data)):
      if int(data[i]) > int(data[i - 1]):
        output += 1

    print(output)

def part_2():
  with open("data.txt") as f:
    data = f.readlines()

    output = 0
    for i in range(1, len(data) - 2):
      first_window = int(data[i - 1]) + int(data[i]) + int(data[i + 1])
      second_window = int(data[i]) + int(data[i + 1]) + int(data[i + 2])

      if first_window < second_window:
        output += 1
    print(output)


if __name__ == "__main__":
  replit_start_time = time.perf_counter()
  """
  Run your functions here.
  This code won't be run if imported.
  """
  part_2()

  # Keep this line at the end of your code
  replit_end_time = time.perf_counter()
  print("Elapsed time:", replit_end_time - replit_start_time)
