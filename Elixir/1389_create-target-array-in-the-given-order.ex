defmodule Solution do
  @spec create_target_array(nums :: [integer], index :: [integer]) :: [integer]
  def create_target_array(nums, index) do
    Enum.zip(nums, index)
    |> Enum.reduce([], fn {num, index}, acc ->
      List.insert_at(acc, index, num)
    end)
  end
end
