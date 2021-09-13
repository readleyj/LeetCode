defmodule Solution do
  @spec min_operations(logs :: [String.t()]) :: integer
  def min_operations(logs) do
    Enum.reduce(logs, 0, fn
      "./", acc -> acc
      "../", 0 -> 0
      "../", acc -> acc - 1
      _, acc -> acc + 1
    end)
  end
end
