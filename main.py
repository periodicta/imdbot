import os
import discord
import json
import keep_alive
from imdb import IMDb
from textwrap import wrap
from discord.ext import commands
from urllib.request import urlopen

keep_alive.keep_alive()

bot = commands.Bot(command_prefix='imdb ')
ia = IMDb()

@bot.command()
async def pop(ctx, medium):
  if medium == "tv":
    movie = ia.get_popular100_tv()[0]
  elif medium == "movie":
    movie = ia.get_popular100_movies()[0]
  else:
    ctx.send("Please give a correct format.")
    return
  ia.update(movie, info=['main','plot'])
  if movie['kind'] == "movie":
    kind="movie"
    name = "*"+str(movie)+"* ("+str(movie['year'])+")"
  elif movie['kind'] in ["tv series","tv mini series"]:
    kind="tv"
    name = "*"+str(movie)+"* ("+str(movie['series years'])+")"

  try:
    rate = movie['rating']
    num = movie['votes']
    rating = round((rate*num+7000)/(num+1000),2)
    if rating >= 9.5: rating = str(rating)+" (Perfection)"
    elif rating >= 9: rating = str(rating)+" (Legendary)"
    elif rating >= 8.5: rating = str(rating)+" (Great)"
    elif rating >= 8: rating = str(rating)+" (Very Good)"
    elif rating >= 7.5: rating = str(rating)+" (Solid)"
    elif rating >= 7: rating = str(rating)+" (Meh)"
    elif rating >= 6.5: rating = str(rating)+" (Poor)"
    elif rating >= 6: rating = str(rating)+" (Very Bad)"
    else: rating = str(rating)+" (Trash)"
  except:
    rating = "N/A"
  try:
    plot = movie['plot'][0].split("::")[0]
  except:
    plot = ""
  try:
    url = urlopen("https://api.themoviedb.org/3/find/tt"+movie["imdbID"]+"?api_key=c52416dfaace6f484472b33aafb87fb4&external_source=imdb_id")
    data = json.loads(url.read())
    img = "http://image.tmdb.org/t/p/original"+data[kind+"_results"][0]["backdrop_path"]
  except:
    img = ""
  try:
    thumb = movie['cover url']
  except:
    thumb = ""
  embed=discord.Embed(
    title=name,
    description="**Adjusted Rating: {}**\n\n{}".format(rating, plot),
    color=0xdba506)
  embed.set_image(url = img)
  embed.set_thumbnail(url = thumb)
  await ctx.send(embed = embed)

@bot.command()
async def search(ctx, name):
  movie = ia.search_movie(name)[0]
  ia.update(movie, info=['main','plot'])
  if movie['kind'] == "movie":
    kind="movie"
    path = "backdrop_path"
    name = "*"+str(movie)+"* ("+str(movie['year'])+")"
  elif movie['kind'] in ["tv series","tv mini series"]:
    kind="tv"
    path = "backdrop_path"
    name = "*"+str(movie)+"* ("+str(movie['series years'])+")"
  elif movie['kind'] == "episode":
    ia.update(movie, info=['episodes'])
    kind="tv_episode"
    path = "still_path"
    name = "*"+str(movie['episode of'])+"*: "+str(movie)+" ("+str(movie['year'])+")"
  try:
    rate = movie['rating']
    num = movie['votes']
    rating = round((rate*num+7000)/(num+1000),2)
    if rating >= 9.5: rating = str(rating)+" (Perfection)"
    elif rating >= 9: rating = str(rating)+" (Legendary)"
    elif rating >= 8.5: rating = str(rating)+" (Great)"
    elif rating >= 8: rating = str(rating)+" (Very Good)"
    elif rating >= 7.5: rating = str(rating)+" (Solid)"
    elif rating >= 7: rating = str(rating)+" (Meh)"
    elif rating >= 6.5: rating = str(rating)+" (Poor)"
    elif rating >= 6: rating = str(rating)+" (Very Bad)"
    else: rating = str(rating)+" (Trash)"
  except:
    rating = "N/A"
  try:
    plot = movie['plot'][0].split("::")[0]
  except:
    plot = ""
  try:
    url = urlopen("https://api.themoviedb.org/3/find/tt"+movie["imdbID"]+"?api_key=c52416dfaace6f484472b33aafb87fb4&external_source=imdb_id")
    data = json.loads(url.read())
    img = "http://image.tmdb.org/t/p/original"+data[kind+"_results"][0][path]
  except:
    img = ""
  try:
    thumb = movie['cover url']
  except:
    thumb = ""
  embed=discord.Embed(
    title=name,
    description="**Adjusted Rating: {}**\n\n{}".format(rating, plot),
    color=0xdba506)
  embed.set_image(url = img)
  embed.set_thumbnail(url = thumb)
  await ctx.send(embed = embed)

@bot.command()
async def altsearch(ctx, arg1, arg2):
  try:
    movie = ia.search_movie(arg1)[int(arg2)]
  except:
    await ctx.send("Please specify a correct index.")
  ia.update(movie, info=['main','plot'])
  if movie['kind'] == "movie":
    kind="movie"
    path = "backdrop_path"
    name = "*"+str(movie)+"* ("+str(movie['year'])+")"
  elif movie['kind'] in ["tv series","tv mini series"]:
    kind="tv"
    path = "backdrop_path"
    name = "*"+str(movie)+"* ("+str(movie['series years'])+")"
  elif movie['kind'] == "episode":
    kind="tv_episode"
    path = "still_path"
    name = "*"+str(movie['episode of'])+"*: "+str(movie)+" ("+str(movie['year'])+")"
  try:
    rate = movie['rating']
    num = movie['votes']
    rating = round((rate*num+7000)/(num+1000),2)
    if rating >= 9.5: rating = str(rating)+" (Perfection)"
    elif rating >= 9: rating = str(rating)+" (Legendary)"
    elif rating >= 8.5: rating = str(rating)+" (Great)"
    elif rating >= 8: rating = str(rating)+" (Very Good)"
    elif rating >= 7.5: rating = str(rating)+" (Solid)"
    elif rating >= 7: rating = str(rating)+" (Meh)"
    elif rating >= 6.5: rating = str(rating)+" (Poor)"
    elif rating >= 6: rating = str(rating)+" (Very Bad)"
    else: rating = str(rating)+" (Trash)"
  except:
    rating = "N/A"
  try:
    plot = movie['plot'][0].split("::")[0]
  except:
    plot = ""
  try:
    url = urlopen("https://api.themoviedb.org/3/find/tt"+movie["imdbID"]+"?api_key=c52416dfaace6f484472b33aafb87fb4&external_source=imdb_id")
    data = json.loads(url.read())
    img = "http://image.tmdb.org/t/p/original"+data[kind+"_results"][0][path]
  except:
    img = ""
  try:
    thumb = movie['cover url']
  except:
    thumb = ""
  embed=discord.Embed(
    title=name,
    description="**Adjusted Rating: {}**\n\n{}".format(rating, plot),
    color=0xdba506)
  embed.set_image(url = img)
  embed.set_thumbnail(url = thumb)
  await ctx.send(embed = embed)

@bot.command()
async def review(ctx, arg):
  movie = ia.search_movie(arg)[0]
  ia.update(movie, info=['main','reviews'])
  lines = wrap(movie['reviews'][0]['content'],1900)
  await ctx.send(str(movie)+" Review")
  for line in lines:
    await ctx.send("||"+line+"||")

@bot.command()
async def episode(ctx, arg, seas, ep):
  show = ia.search_movie(arg)[0]
  ia.update(show, info = ['episodes'])
  movie = show['episodes'][int(seas)][int(ep)]
  ia.update(movie, info=['main','plot'])
  kind="tv_episode"
  path = "still_path"
  name = "*"+str(show)+"*: "+str(movie)+" ("+str(movie['year'])+")"
  try:
    rate = movie['rating']
    num = movie['votes']
    rating = round((rate*num+7000)/(num+1000),2)
    if rating >= 9.5: rating = str(rating)+" (Perfection)"
    elif rating >= 9: rating = str(rating)+" (Legendary)"
    elif rating >= 8.5: rating = str(rating)+" (Great)"
    elif rating >= 8: rating = str(rating)+" (Very Good)"
    elif rating >= 7.5: rating = str(rating)+" (Solid)"
    elif rating >= 7: rating = str(rating)+" (Meh)"
    elif rating >= 6.5: rating = str(rating)+" (Poor)"
    elif rating >= 6: rating = str(rating)+" (Very Bad)"
    else: rating = str(rating)+" (Trash)"
  except:
    rating = "N/A"
  try:
    plot = movie['plot'][0].split("::")[0]
  except:
    plot = ""
  try:
    url = urlopen("https://api.themoviedb.org/3/find/tt"+movie["imdbID"]+"?api_key=c52416dfaace6f484472b33aafb87fb4&external_source=imdb_id")
    data = json.loads(url.read())
    img = "http://image.tmdb.org/t/p/original"+data[kind+"_results"][0][path]
  except:
    img = ""
  try:
    thumb = movie['cover url']
  except:
    thumb = ""
  embed=discord.Embed(
    title=name,
    description="**Adjusted Rating: {}**\n\n{}".format(rating, plot),
    color=0xdba506)
  embed.set_image(url = img)
  embed.set_thumbnail(url = thumb)
  await ctx.send(embed = embed)

@bot.command()
async def season(ctx, arg, seas):
  show = ia.search_movie(arg)[0]
  ia.update(show, info = ['episodes'])
  season = show['episodes'][int(seas)]
  info = ""
  ratings = [7]
  years = []
  for id, movie in zip(season.keys(),season.values()):
    try:
      rate = movie['rating']
      num = movie['votes']
      rating = round((rate*num+7000)/(num+1000),2)
      if rating >= 9.5:
        desc = str(rating)+" (Perfection)"
        mod = "**__"
      elif rating >= 9:
        desc = str(rating)+" (Legendary)"
        mod = "**__"
      elif rating >= 8.5:
        desc = str(rating)+" (Great)"
        mod = "**"
      elif rating >= 8:
        desc = str(rating)+" (Very Good)"
        mod = "**"
      elif rating >= 7.5:
        desc = str(rating)+" (Solid)"
        mod = ""
      elif rating >= 7:
        desc = str(rating)+" (Meh)"
        mod = ""
      elif rating >= 6.5:
        desc = str(rating)+" (Poor)"
        mod = "*"
      elif rating >= 6:
        desc = str(rating)+" (Very Bad)"
        mod = "*"
      else:
        desc = str(rating)+" (Trash)"
        mod = "*"
    except:
      rating = desc = "N/A"
    info += "{3}{0}. {1}: {2}{4}\n".format(id, movie, desc,mod,mod[::-1])
    ratings.append(rating)
    years.append(movie['year'])
  
  summing = [rating for rating in ratings if rating != "N/A"]
  overall = round(sum(summing)/len(summing),2)
  if overall >= 9: overall = str(overall)+" (Perfection)"
  elif overall >= 8.5: overall = str(overall)+" (Legendary)"
  elif overall >= 8: overall = str(overall)+" (Great)"
  elif overall >= 7.6: overall = str(overall)+" (Very Good)"
  elif overall >= 7.3: overall = str(overall)+" (Solid)"
  elif overall >= 7: overall = str(overall)+" (Meh)"
  elif overall >= 6.7: overall = str(overall)+" (Poor)"
  elif overall >= 6.4: overall = str(overall)+" (Very Bad)"
  else: overall = str(overall)+" (Trash)"
  early = min(years)
  late = max(years)
  if early == late: span = str(early)
  else: span = str(early)+"-"+str(late)
  try:
    url = urlopen("https://api.themoviedb.org/3/find/tt"+show.movieID+"?api_key=c52416dfaace6f484472b33aafb87fb4&external_source=imdb_id")
    data = json.loads(url.read())
    id = str(data["tv_results"][0]["id"])
    url2 = urlopen("https://api.themoviedb.org/3/tv/"+id+"/season/"+seas+"?api_key=c52416dfaace6f484472b33aafb87fb4")
    data2 = json.loads(url2.read())
    thumb = "http://image.tmdb.org/t/p/original"+data2["poster_path"]
    fixed = [rating if rating != "N/A" else 0 for rating in ratings]
    best = ratings.index(max(fixed)) - 1
  except:
    thumb = ""
  try:
    url = urlopen("https://api.themoviedb.org/3/find/tt"+list(season.values())[best].movieID+"?api_key=c52416dfaace6f484472b33aafb87fb4&external_source=imdb_id")
    data = json.loads(url.read())
    img = "http://image.tmdb.org/t/p/original"+data["tv_episode_results"][0]["still_path"]
  except:
    img = ""
  embed=discord.Embed(
    title="*"+str(show)+"* Season "+seas+" ("+span+")",
    description="**Average Adjusted Rating: "+overall+"**\n\n"+info,
    color=0xdba506)
  embed.set_image(url = img)
  embed.set_thumbnail(url = thumb)
  await ctx.send(embed = embed)

bot.run(os.getenv('token'))
