defmodule Solution do
  @spec reverse_words(s :: String.t()) :: String.t()
  def reverse_words(s) do
    String.split(s, " ") |> Enum.map_join(" ", &String.reverse(&1))
  end
end
