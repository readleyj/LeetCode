defmodule Solution do
  @spec kids_with_candies(candies :: [integer], extra_candies :: integer) :: [boolean]
  def kids_with_candies(candies, extra_candies) do
    max_candies = Enum.max(candies)

    Enum.map(candies, &(&1 + extra_candies >= max_candies))
  end
end
