const db = require('./db');
const { ApolloError } = require('apollo-server-express');

import { sortArrayByDate } from './utils/date-sort';
import { publish } from './utils/MQService';

const lightsDbColumn = 'light_plan';

export default {
  Query: {
    setting: (parent: any, args: { name: string }): object => {
      const text = 'SELECT * FROM user_settings WHERE name = $1';
      const values = [args.name];
      return db
        .query(text, values)
        .then((res: any) => {
          const row = res.rows[0];
          return row;
        })
        .catch((e: any) => {
          console.log(e);
          throw new ApolloError(e.message);
        });
    },
    lightPlan: (): LightPlan => {
      const text = 'SELECT * FROM user_settings WHERE name = $1';
      const values = [lightsDbColumn];
      return db
        .query(text, values)
        .then((res: any) => {
          const row = res.rows[0];
          return row;
        })
        .catch((e: any) => {
          console.log(e);
          throw new ApolloError(e.message);
        });
    },
  },
  Mutation: {
    updateLightPlan: (parent: any, args: LightPlan): object => {
      const text = 'UPDATE user_settings SET value = $1 WHERE name= $2 RETURNING *';
      args.value.sort(sortArrayByDate);
      const plan = JSON.stringify(args.value);
      const values = [plan, lightsDbColumn];

      return db
        .query(text, values)
        .then((res: any) => {
          publish(lightsDbColumn, plan);
          const row = res.rows[0];
          return row;
        })
        .catch((e: any) => {
          console.log(e);
          throw new ApolloError(e.message);
        });
    },
  },
};
