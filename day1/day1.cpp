#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>

int main() {

  std::ifstream input("../input.txt");

  if (!input) {
    std::cerr << "Could not open input.txt.\n";
    return 1;
  }

  std::vector<size_t> elves_with_calories;
  size_t index = 0;

  std::string line;
  while (std::getline(input, line)) {
    if (line.empty()) {
        index++;
        continue;
    }

    size_t calories = std::stoi(line);

    if (elves_with_calories.size() < index + 1) {
        elves_with_calories.emplace_back(calories);
    } else {
        elves_with_calories[index] += calories;
    }
  }

  std::sort(elves_with_calories.begin(), elves_with_calories.end(), [](size_t a, size_t b){
      return a > b;
  });


  size_t sum = std::accumulate(elves_with_calories.begin(), elves_with_calories.begin() + 3, 0);

  std::cout << "Top elf has " << elves_with_calories[0] << " calories, top 3 elves have " << sum << " calories together.\n";

  return 0;
}