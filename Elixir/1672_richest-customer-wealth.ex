defmodule Solution do
  @spec maximum_wealth(accounts :: [[integer]]) :: integer
  def maximum_wealth(accounts) do
    Enum.reduce(accounts, 0, fn x, max_wealth -> max(max_wealth, Enum.sum(x)) end)
  end
end
