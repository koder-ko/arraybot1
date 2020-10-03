import discord
import openpyxl
import asyncio
from json import loads
import random

client = discord.Client()



@client.event
async def on_raw_reaction_add(payload):
  if payload.emoji == "👍":
      print("wa")

client.run('NzYxOTQxMzMyNjc0NzQwMjI0.X3h7KQ.dkSTjJNYnRzM0YsYajPr4sYyTiw')