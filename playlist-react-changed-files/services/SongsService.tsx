import { ISongData } from "../interfaces/ISongData";
import axios from "../axios-setup";
import { AxiosResponse } from "axios";
import { IPlayListData } from "../interfaces/IPlayListData";
export const sendSong = (song: ISongData) => {
  try {
    return axios.post<ISongData>("/addSong", song);
  } catch (err) {
    alert("Save Failed");
    console.log(err);
  }
};
export const addPlaylist = (playlist: IPlayListData) => {
  try {
    return axios.post<IPlayListData>("/addPlaylist", playlist);
  } catch (err) {
    alert("Save Failed");
    console.log(err);
  }
};

export const deleteSong = (songID: number) => {
  try {
    return axios.delete<ISongData>("/deleteSong/" + songID);
  } catch (err) {
    alert("Delete Failed");
    console.log(err);
  }
};

export const deletePlayList = (playListID: number) => {
  try {
    return axios.delete<IPlayListData>("/deletePlaylist/" + playListID);
  } catch (err) {
    alert("Delete Failed");
    console.log(err);
  }
};

export const getAllSongs = async () => {
  try {
    const response = await axios.get<ISongData,AxiosResponse<Array<ISongData>>>("/getAllSongs");
    return response.data;
  } catch (err) {
    alert("Get Failed");
    console.log(err);
  }
};

export const getAllPlayLists = async () => {
  try {
    const response = await axios.get<
      IPlayListData,
      AxiosResponse<Array<IPlayListData>>
    >("/getAllPlaylist");
    return response.data;
  } catch (err) {
    alert("Get Failed");
    console.log(err);
  }
};

export const deleteSongFromPlayList = (playListID: number, songID: number) => {
  try {
    return axios.delete<ISongData>(
      "/deletePlaylistSongMapping/" + playListID + "/" + songID
    );
  } catch (err) {
    alert("Delete Failed");
    console.log(err);
  }
};

export const addSongToPlayList = async (songID: number, playListID: number) => {
  try {
    //changes done here!
    let formData = new FormData();     
    formData.append('playlistId', playListID.toString());
    formData.append('songId', songID.toString());

    console.log("song id " + songID + " pid " + playListID)

    // const response = await axios.post<IPlayListData>(
    //   "/addPlaylistSongMapping/" + playListID + "/" + songID
    // );

    const response = await axios.post(
      "/addPlaylistSongMapping",
      formData
    );

    console.log("-- response data --")
    console.log(response.data);
    console.log(response.data['status']);
    console.log("-- response status --")
    console.log(response.status)
    return response.data;
  } catch (err) {
    alert("Get Failed");
    console.log(err);
    console.log("song id " + songID + " pid " + playListID)
  }
};

export const getAllSongFromPlayList = async (playListID: number) => {
  try {
    const response = await axios.get<ISongData, AxiosResponse<Array<ISongData>>
    >("/getAllPlaylistSongs/" + playListID);

    console.log("-- get all songs -- " + response.data[0])
  
    return response.data;
  } catch (err) {
    alert("Get Failed");
    console.log(err);
  }
};
