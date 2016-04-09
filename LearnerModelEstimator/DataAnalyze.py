{
 "metadata": {
  "name": ""
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import pandas as pd\n",
      "import numpy as np\n",
      "import datetime"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 227
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat = pd.read_table(\"algebra_2006_2007/algebra_2006_2007_master.txt\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 78
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat.columns = dat.columns.str.replace(\" \",\"_\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 79
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "sample_data = dat[dat.Anon_Student_Id=='W1SLytJ']"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "s\n",
      "sample_data.Correct_First_Attempt.hist()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "NameError",
       "evalue": "name 's' is not defined",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-35-3b842723e162>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0ms\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0msample_data\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCorrect_First_Attempt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;31mNameError\u001b[0m: name 's' is not defined"
       ]
      }
     ],
     "prompt_number": 35
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "points = (dat.Corrects-dat.Incorrects).sum()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 127
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "points"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 128,
       "text": [
        "12470"
       ]
      }
     ],
     "prompt_number": 128
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat.insert(2,\"Point\", points)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "ValueError",
       "evalue": "cannot insert Point, already exists",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-175-b79b1f0db539>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"Point\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpoints\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/pandas/core/frame.pyc\u001b[0m in \u001b[0;36minsert\u001b[0;34m(self, loc, column, value, allow_duplicates)\u001b[0m\n\u001b[1;32m   2438\u001b[0m         \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sanitize_column\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcolumn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2439\u001b[0m         self._data.insert(loc, column, value,\n\u001b[0;32m-> 2440\u001b[0;31m                           allow_duplicates=allow_duplicates)\n\u001b[0m\u001b[1;32m   2441\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2442\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0massign\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/pandas/core/internals.pyc\u001b[0m in \u001b[0;36minsert\u001b[0;34m(self, loc, item, value, allow_duplicates)\u001b[0m\n\u001b[1;32m   3443\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mallow_duplicates\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mitem\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3444\u001b[0m             \u001b[0;31m# Should this be a different kind of error??\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3445\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'cannot insert %s, already exists'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mitem\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3446\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3447\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;31mValueError\u001b[0m: cannot insert Point, already exists"
       ]
      }
     ],
     "prompt_number": 175
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "data_per_quiz = dat.groupby([\"Problem_Name\",\"Anon_Student_Id\"])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 129
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "matrix = pd.DataFrame(columns=dat.Anon_Student_Id.unique(),index=dat[\"Problem_Name\"].unique())"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 121
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "for name,quiz in data_per_quiz:\n",
      "    problem_name,student_id = name\n",
      "    points = (quiz.Corrects-quiz.Incorrects).sum()\n",
      "    matrix.loc[problem_name,student_id]=points"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat['Step_End_Time'] = pd.to_datetime(dat['Step_End_Time'])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat['Step_Start_Time'] = pd.to_datetime(dat['Step_Start_Time'])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "duration_quiz = dat.Step_End_Time - dat.Step_Start_Time"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 164
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "duration_quiz.to_json(\"quiz_per_duration.json\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 171
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "problems_feature = pd.DataFrame(columns=[\"Average_Time_Response\",\"Average_Attemps\",\"Average_Student_First_Time_Correct\",\"Total_Students_Attemps\"],index=dat[\"Problem_Name\"].unique())"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 173
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "s = dat.groupby([\"Anon_Student_Id\"]).sum()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 196
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "%matplotlib\n",
      "s.Point.hist()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Using matplotlib backend: TkAgg\n"
       ]
      },
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 202,
       "text": [
        "<matplotlib.axes.AxesSubplot at 0x7f2b78be3250>"
       ]
      }
     ],
     "prompt_number": 202
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "s.Point.to_json(\"points_per_student.json\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 201
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "t = dat.groupby([\"Anon_Student_Id\"]).count()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 204
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "profile_student = dat[dat.Anon_Student_Id=='W1SLytJ']"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 221
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "points_per_student = profile_student.Point"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 225
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat['Step_End_Time'] = dat[\"Step_End_Time\"].apply( lambda dat : datetime.datetime(year=dat.year, month=dat.month, day=dat.day)) "
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 228
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat.set_index(dat[\"Step_End_Time\"],inplace=True)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 229
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "points_per_day = dat['Point'].resample('D').sum()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 253
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "%matplotlib\n",
      "points_per_day[\"2006-09-05\":\"2007-07-20\"].plot()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Using matplotlib backend: TkAgg\n"
       ]
      },
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 264,
       "text": [
        "<matplotlib.axes.AxesSubplot at 0x7f2b63ba1390>"
       ]
      }
     ],
     "prompt_number": 264
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "example_responses = dat[[\"Anon_Student_Id\",\"Step_Name\",\"Correct_First_Attempt\",u\"Step_Duration_(sec)\"]][2:]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 277
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "example_responses.to_json(\"example_responses.json\",orient=\"records\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 279
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dat.columns"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 273,
       "text": [
        "Index([u'Row', u'Anon_Student_Id', u'Point', u'Problem_Hierarchy',\n",
        "       u'Problem_Name', u'Problem_View', u'Step_Name', u'Step_Start_Time',\n",
        "       u'First_Transaction_Time', u'Correct_Transaction_Time',\n",
        "       u'Step_End_Time', u'Step_Duration_(sec)',\n",
        "       u'Correct_Step_Duration_(sec)', u'Error_Step_Duration_(sec)',\n",
        "       u'Correct_First_Attempt', u'Incorrects', u'Hints', u'Corrects',\n",
        "       u'KC(Default)', u'Opportunity(Default)'],\n",
        "      dtype='object')"
       ]
      }
     ],
     "prompt_number": 273
    }
   ],
   "metadata": {}
  }
 ]
}