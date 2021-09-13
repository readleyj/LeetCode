defmodule Solution do
  @spec three_consecutive_odds(arr :: [integer]) :: boolean
  def three_consecutive_odds(arr) do
    Enum.reduce_while(arr, 0, fn num, acc ->
      cond do
        acc >= 3 -> {:halt, acc}
        rem(num, 2) == 1 -> {:cont, acc + 1}
        rem(num, 2) == 0 -> {:cont, 0}
      end
    end) >= 3
  end
end
