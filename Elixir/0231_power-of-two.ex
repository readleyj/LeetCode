defmodule Solution do
  use Bitwise

  @spec is_power_of_two(n :: integer) :: boolean
  def is_power_of_two(n) do
    n != 0 and Bitwise.band(n, n - 1) == 0
  end
end
