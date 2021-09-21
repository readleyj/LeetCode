defmodule Solution do
  @spec group_the_people(group_sizes :: [integer]) :: [[integer]]
  def group_the_people(group_sizes) do
    Enum.with_index(group_sizes)
    |> Enum.reduce(Map.new(), fn {size, idx}, acc ->
      Map.update(acc, size, [idx], fn group -> [idx | group] end)
    end)
    |> Enum.flat_map(fn {size, group} ->
      Enum.chunk_every(group, size)
    end)
  end
end
