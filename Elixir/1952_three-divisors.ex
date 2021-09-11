defmodule Solution do
  @spec is_three(n :: integer) :: boolean
  def is_three(n) do
    Enum.count(1..n, &(rem(n, &1) == 0)) == 3
  end
end
