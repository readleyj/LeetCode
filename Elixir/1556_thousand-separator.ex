defmodule Solution do
  @spec thousand_separator(n :: integer) :: String.t()
  def thousand_separator(n) do
    Integer.to_string(n)
    |> String.graphemes()
    |> Enum.reverse()
    |> Enum.chunk_every(3)
    |> Enum.intersperse(".")
    |> Enum.join()
    |> String.graphemes()
    |> Enum.reverse()
    |> Enum.join()
  end
end
