#!/usr/bin/node
const request = require('request');

const baseURL = process.argv[2];
const userURL = baseURL.replace('todos', 'users');

/*
 - Get all users and append their ids into an array.
 - Fetch all todos per user and see if the attribute completed is True.
 - Append the number of completed todos per user.
 - Only log the dict representing the user id and completed todos when all counts
   are added to the todDict.
*/

request(userURL, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  const users = JSON.parse(body);
  const userIds = [];
  const todosDict = {};
  for (const user of users) {
    userIds.push(user.id);
  }
  for (let i = 0; i < userIds.length; i++) {
    const todoURL = `${userURL}/${userIds[i]}/todos`;
    request(todoURL, function (error, response, body) {
      if (error) {
        throw new Error(error);
      }
      const todos = JSON.parse(body);
      let count = 0;
      for (let i = 0; i < todos.length; i++) {
        if (todos[i].completed === true) {
          count += 1;
        }
      }
      const key = userIds[i];
      todosDict[key] = count;
      if (Object.keys(todosDict).length === userIds.length) {
        console.log(todosDict);
      }
    });
  }
});
