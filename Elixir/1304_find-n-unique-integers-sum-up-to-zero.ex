defmodule Solution do
  @spec sum_zero(n :: integer) :: [integer]
  def sum_zero(n) do
    case n do
      1 -> [0]
      _ -> Enum.flat_map(1..div(n, 2), &[&1, -&1]) ++ if rem(n, 2) == 1, do: [0]
    end
  end
end
