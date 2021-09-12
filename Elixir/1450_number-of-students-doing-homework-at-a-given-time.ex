defmodule Solution do
  @spec busy_student(start_time :: [integer], end_time :: [integer], query_time :: integer) ::
          integer
  def busy_student(start_time, end_time, query_time) do
    Enum.zip(start_time, end_time)
    |> Enum.count(fn {start_time, end_time} ->
      query_time >= start_time and query_time <= end_time
    end)
  end
end
