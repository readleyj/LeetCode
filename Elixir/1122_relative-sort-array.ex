defmodule Solution do
  @spec relative_sort_array(arr1 :: [integer], arr2 :: [integer]) :: [integer]
  def relative_sort_array(arr1, arr2) do
    index_map = Enum.with_index(arr2) |> Enum.into(%{})

    Enum.sort_by(arr1, &{index_map[&1], &1})
  end
end
