defmodule Solution do
  @spec is_covered(ranges :: [[integer]], left :: integer, right :: integer) :: boolean
  def is_covered(ranges, left, right) do
    value_set =
      Enum.reduce(ranges, MapSet.new(), fn [start_i, end_i], acc ->
        Enum.reduce(start_i..end_i, acc, &MapSet.put(&2, &1))
      end)

    Enum.all?(left..right, &MapSet.member?(value_set, &1))
  end
end
