leap_year :: Int -> Bool
leap_year x = (x `mod` 4 == 0) && (not (x `mod` 100 == 0) || (x `mod` 400 == 0))

months :: Int -> [Int]
months year | leap_year year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            | otherwise = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sundays :: Int -> [Int] -> Int
sundays wkd ms | ms == [] = 0
               | otherwise = x + sundays wkd' ms'
                 where
                   d = head ms
                   ms' = tail ms
                   wkd' = (d - ((7 - wkd) `mod` 7)) `mod` 7
                   x = if wkd == 0 then 1 else 0

sunday_counter :: Int -> Int -> Int -> Int
sunday_counter weekday year end_year | year == end_year = 0
                                     | otherwise = x + sunday_counter weekday' (year+1) end_year
                                       where
                                         ms = months year
                                         d = sum ms
                                         weekday' = (d - ((7 - weekday) `mod` 7)) `mod` 7
                                         x = sundays weekday ms
                                         
