defmodule Solution do
  @spec reverse_str(s :: String.t(), k :: integer) :: String.t()
  def reverse_str(s, k) do
    Enum.chunk_every(String.graphemes(s), 2 * k)
    |> Enum.flat_map(fn chunk -> Enum.reverse_slice(chunk, 0, k) end)
    |> Enum.join()
  end
end
