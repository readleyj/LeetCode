defmodule Solution do
  @spec longest_common_prefix(strs :: [String.t()]) :: String.t()
  def longest_common_prefix(strs) do
    Enum.map(strs, &String.graphemes/1)
    |> Enum.zip()
    |> Enum.map(&Tuple.to_list/1)
    |> Enum.reduce_while("", fn chars, acc ->
      first_char = Enum.at(chars, 0)
      if Enum.all?(chars, &(&1 == first_char)), do: {:cont, acc <> first_char}, else: {:halt, acc}
    end)
  end
end
