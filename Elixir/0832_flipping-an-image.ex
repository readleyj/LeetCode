defmodule Solution do
  @spec flip_and_invert_image(image :: [[integer]]) :: [[integer]]
  def flip_and_invert_image(image) do
    Enum.map(image, &Enum.reverse/1)
    |> Enum.map(fn row ->
      Enum.map(row, &(1 - &1))
    end)
  end
end
