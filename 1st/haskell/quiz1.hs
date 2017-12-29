module Main (main) where

main :: IO ()
main = print(sumList 20)

sumList::Int->Int
sumList n = sum [2*x - 1 | x <- [1..n]]
