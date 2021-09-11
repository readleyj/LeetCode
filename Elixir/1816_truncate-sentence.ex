defmodule Solution do
  @spec truncate_sentence(s :: String.t(), k :: integer) :: String.t()
  def truncate_sentence(s, k) do
    String.split(s) |> Enum.slice(0..(k - 1)) |> Enum.join(" ")
  end
end
